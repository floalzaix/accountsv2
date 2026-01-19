import { Component, effect, inject, OnInit, signal } from '@angular/core';
import { CategoryComponent } from '../category.component/category.component';
import { CardModule } from 'primeng/card';
import { CategoriesService } from '../categories.service';
import { Category } from '../categories.model';
import { InplaceModule } from 'primeng/inplace';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AutoFocusModule } from 'primeng/autofocus';
import { ButtonModule } from 'primeng/button';
import { ErrorWrapper } from '../../shared/errors/error-wrapper';
import { MessageService } from 'primeng/api';
import { ToastModule } from 'primeng/toast';
import { closeInplaceForm } from '../../shared/utils/other';

@Component({
  selector: 'app-categories-component',
  imports: [
    CategoryComponent,
    CardModule,
    InplaceModule,
    ReactiveFormsModule,
    AutoFocusModule,
    ButtonModule,
    ToastModule,
  ],
  templateUrl: './categories.component.html',
  styleUrl: './categories.component.css',
  providers: [MessageService],
})
export class CategoriesComponent implements OnInit {
  closeInplaceForm = closeInplaceForm;

  //
  //   Interfaces
  //
  
  private readonly categoriesService = inject(CategoriesService);
  private readonly messageService = inject(MessageService);

  //
  //   Data
  //
  
  public categories = signal<Category[]>([]);

  //
  //   Forms
  //
  
  public addCategoryForm = new FormGroup({
    name: new FormControl<string>('', [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
  });

  //
  //   Init
  //
  
  ngOnInit(): void {
    this.getAllCategories();
  }

  //
  //   State Machines
  //

  public readonly categoriesStateLevel = signal<number>(0);

  protected readonly level1SelectedCategory = signal<string | null>(null);
  protected readonly level2SelectedCategory = signal<string | null>(null);
  protected readonly level3SelectedCategory = signal<string | null>(null);
  
  // State handlers

  protected readonly handleCategoriesStateLevel = effect(() => {
    // Making level 2 categories appear if a level 1 is selected
    if (this.level1SelectedCategory() !== null) {
      this.categoriesStateLevel.set(1);
    } else {
      // If no level 1 is selected, we reset the level 2 and 3 categories
      // to prevent disabled categories from appearing
      this.level2SelectedCategory.set(null);
      this.level3SelectedCategory.set(null);
    }
    
    // Same process for level 2 categories
    if (this.level2SelectedCategory() !== null) {
      this.categoriesStateLevel.set(2);
    } else {
      this.level3SelectedCategory.set(null);
    }

    // Same process for level 3 categories
    if (this.level3SelectedCategory() !== null) {
      this.categoriesStateLevel.set(3);
    }
    
    // Resetting if no level is selected
    if (this.level1SelectedCategory() === null) {
      this.categoriesStateLevel.set(0);
    }
  });

  //
  //   Methods
  //
  
  /**
   * Fetches all categories from the backend.
   */
  public getAllCategories(): void {
    this.categoriesService.getAllCategories().subscribe({
      next: (categories) => {
        this.categories.set(categories);
      },
    });
  }

  /**
   * Adds a new category to the database.
   */
  public addCategory(): void {
    // Looking for the parent category and therefore the level
    let parent_id = null;
    let level = 0;

    if (this.level1SelectedCategory()) {
      parent_id = this.level1SelectedCategory();
      level = 1;
    } 
    if (this.level2SelectedCategory()) {
      parent_id = this.level2SelectedCategory();
      level = 2;
    } 
    if (this.level3SelectedCategory()) {
      throw new Error('Cannot add a category to a level 3 category');
    }

    // Validating the data
    if (this.addCategoryForm.invalid) {
      this.addCategoryForm.markAllAsTouched();
      this.messageService.add({
        severity: 'error',
        summary: 'Erreur',
        detail: 'Le nom est invalide !',
        life: 3000,
      });
      
      return;
    }

    // Adding the category
    this.categoriesService.addCategory({
      name: this.addCategoryForm.value.name!,
      level,
      parent_id,
    }).subscribe({
      next: () => {

        this.messageService.add({
          severity: 'success',
          summary: 'Succès',
          detail: 'Catégorie ajoutée avec succès !',
          life: 2000,
        });

        // Refreshing the categories system.
        this.addCategoryForm.reset();
        this.getAllCategories();
      },
      error: (error) => {
        if (error instanceof ErrorWrapper) {
          this.messageService.add({
            severity: 'error',
            summary: error.userSafeTitle,
            detail: error.userSafeDescription,
            life: 3000,
          });
        }

        throw error;
      },
    });
  }
}
