import { Component, inject } from '@angular/core';
import { CategoriesComponent } from '../../../categories/categories.component/categories.component';
import { TransactionsTable } from '../../../transactions/trans-table.component/trans-table.component';
import { TransactionAddBar } from '../../../transactions/trans-add-bar.component/trans-add-bar.component';
import { Options } from '../../components/options/options';
import { DetailsTab } from '../../../details/details-tab/details-tab';
import { OptionsService } from '../../services/options';

@Component({
  selector: 'app-home-page',
  imports: [
    CategoriesComponent,
    TransactionsTable,
    TransactionAddBar,
    Options,
    DetailsTab
  ],
  templateUrl: './home.page.html',
  styleUrl: './home.page.css',
})
export class HomePage {
  //
  //   Inputs
  //
  
  protected readonly optionsService = inject(OptionsService);
}
