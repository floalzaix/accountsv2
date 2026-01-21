import { Component } from '@angular/core';
import { CategoriesComponent } from '../../../categories/categories.component/categories.component';
import { TransactionsTable } from '../../../transactions/trans-table.component/trans-table.component';
import { TransactionAddBar } from '../../../transactions/trans-add-bar.component/trans-add-bar.component';

@Component({
  selector: 'app-home-page',
  imports: [
    CategoriesComponent,
    TransactionsTable,
    TransactionAddBar
  ],
  templateUrl: './home.page.html',
  styleUrl: './home.page.css',
})
export class HomePage {

}
