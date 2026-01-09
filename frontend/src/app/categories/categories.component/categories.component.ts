import { Component, inject, OnInit, signal } from '@angular/core';
import { CategoryComponent } from '../category.component/category.component';
import { CardModule } from 'primeng/card';
import { CategoriesService } from '../categories.service';
import { Category } from '../categories.model';
import { InplaceModule } from 'primeng/inplace';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';

@Component({
  selector: 'app-categories-component',
  imports: [
    CategoryComponent,
    CardModule,
    InplaceModule,
    ReactiveFormsModule,
    InputTextModule,
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
