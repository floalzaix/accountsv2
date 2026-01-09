import { Component, input } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { Category } from '../categories.model';

@Component({
  selector: 'app-category-component',
  imports: [
    ButtonModule,
    CardModule,
  ],
  templateUrl: './category.component.html',
  styleUrl: './category.component.css',
})
export class CategoryComponent {
  //
  //   Interfaces
  //
  
  public readonly category = input.required<Category>();
}
