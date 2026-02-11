import { Component } from '@angular/core';
import { BalanceComponent } from '../../../summary/balance.component/balance.component';

@Component({
  selector: 'app-summary.page',
  imports: [
    BalanceComponent,
  ],
  templateUrl: './summary.page.html',
  styleUrl: './summary.page.css',
})
export class SummaryPage {

}
