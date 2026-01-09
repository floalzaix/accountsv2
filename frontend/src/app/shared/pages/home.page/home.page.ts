import { Component } from '@angular/core';
import { CategoriesComponent } from '../../../categories/categories.component/categories.component';

@Component({
  selector: 'app-home-page',
  imports: [CategoriesComponent],
  templateUrl: './home.page.html',
  styleUrl: './home.page.css',
})
export class HomePage {

}
