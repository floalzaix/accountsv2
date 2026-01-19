import { Component } from '@angular/core';
import { CategoriesComponent } from '../../../categories/categories.component/categories.component';
import { TransactionsTable } from '../../../transactions/trans-table.component/trans-table.component';

@Component({
  selector: 'app-home-page',
  imports: [
    CategoriesComponent,
    TransactionsTable
  ],
  templateUrl: './home.page.html',
  styleUrl: './home.page.css',
})
export class HomePage {

}
