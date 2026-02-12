import { Component, computed, inject, input, model, output, signal } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { Category, CategoryState } from '../categories.model';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AutoFocusModule } from 'primeng/autofocus';
import { closeInplaceForm } from '../../shared/utils/other';
import { InplaceModule } from 'primeng/inplace';
import { CategoriesService } from '../categories.service';
import { MessageService } from 'primeng/api';
import { ToastModule } from 'primeng/toast';
import { ErrorWrapper } from '../../shared/errors/error-wrapper';

@Component({
  selector: 'app-category-component',
  imports: [
    ButtonModule, 
    CardModule,
    ReactiveFormsModule,
    AutoFocusModule,
    InplaceModule,
    ToastModule,
  ],
  templateUrl: './category.component.html',
  styleUrl: './category.component.css',
  providers: [MessageService],
})
export class CategoryComponent {
  closeInplaceForm = closeInplaceForm;

  //
  //   Interfaces
  //

  private  readonly messageService = inject(MessageService);
  private  readonly categoriesService = inject(CategoriesService);

  public readonly category = input.required<Category>();

  public readonly onUpdated = output<void>();

  //
  //   Forms
  //
  
  protected readonly editCategoryForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', [Validators.required, Validators.minLength(1), Validators.maxLength(255)]),
  });

  //
  //   Computed properties
  //
  
  public readonly color = computed(() => {
    switch (this.category().level) {
      case 0:
        return "black";
      case 1:
        return "var(--secondary-color)";
      case 2:
        return "var(--primary-color-darker)";
      default:
        throw new Error('Invalid category level');
    };
  });

  //
  //   State Machine
  //

  public readonly state = model<CategoryState>();
  public readonly isEditing = signal<boolean>(false);
  public readonly isDeleting = signal<boolean>(false);

  //
  //   Methods
  //
  
  public editCategory(): void {
    // Validating the data
    if (this.editCategoryForm.invalid) {
      this.editCategoryForm.markAllAsTouched();
      this.messageService.add({
        severity: 'error',
        summary: 'Erreur',
        detail: 'Le nom est invalide !',
        life: 3000,
      });
      return;
    }

    // Editing the category
    this.categoriesService.editCategory(
      this.category().id, this.editCategoryForm.value.name
    ).subscribe({
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Succès',
          detail: 'La catégorie a été modifiée avec succès !',
          life: 2000,
        });

        this.onUpdated.emit();
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

  public deleteCategory(): void {
    this.categoriesService.deleteCategory(this.category().id).subscribe({
      next: () => {
        this.messageService.add({
          severity: 'success',
          summary: 'Succès',
          detail: 'La catégorie a été supprimée avec succès !',
          life: 2000,
        });

        this.onUpdated.emit();
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
