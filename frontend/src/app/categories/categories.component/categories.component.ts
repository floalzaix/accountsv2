import { Component } from '@angular/core';
import { CatgoryComponent } from '../catgory.component/catgory.component';
import { ButtonGroupModule } from 'primeng/buttongroup';

@Component({
  selector: 'app-categories-component',
  imports: [
    CatgoryComponent,
  ],
  templateUrl: './categories.component.html',
  styleUrl: './categories.component.css',
})
export class CategoriesComponent {

}
