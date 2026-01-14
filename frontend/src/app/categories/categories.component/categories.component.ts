import { Component, effect, inject, OnInit, signal } from '@angular/core';
import { CategoryComponent } from '../category.component/category.component';
import { CardModule } from 'primeng/card';
import { CategoriesService } from '../categories.service';
import { Category } from '../categories.model';
import { InplaceModule } from 'primeng/inplace';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AutoFocusModule } from 'primeng/autofocus';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-categories-component',
  imports: [
    CategoryComponent,
    CardModule,
    InplaceModule,
    ReactiveFormsModule,
    AutoFocusModule,
    ButtonModule,
  ],
  templateUrl: './categories.component.html',
  styleUrl: './categories.component.css',
})
export class CategoriesComponent implements OnInit {
  //
  //   Interfaces
  //
  
  private readonly categoriesService = inject(CategoriesService);

  //
  //   Data
  //
  
  public categories = signal<Category[]>([]);

  //
  //   Forms
  //
  
  public addCategoryForm = new FormGroup({
    name: new FormControl('', [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
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
    console.log('addCategory');
  }
}
