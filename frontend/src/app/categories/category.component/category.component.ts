import { Component, computed, input, model, output } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';
import { Category, CategoryState } from '../categories.model';

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

  //
  //   Computed properties
  //
  
  public readonly color = computed(() => {
    switch (this.category().level) {
      case 0:
        return "blue";
      case 1:
        return "black";
      case 2:
        return "red";
      default:
        throw new Error('Invalid category level');
    };
  });

  //
  //   State Machine
  //

  public readonly state = model<CategoryState>();
}
