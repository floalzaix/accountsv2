import { Component } from '@angular/core';
import { MenuBar } from '../../components/menu-bar/menu-bar';
import { MenuCol } from '../../components/menu-col/menu-col';
import { BalanceComponent } from '../../../summary/balance.component/balance.component';

@Component({
  selector: 'app-summary.page',
  imports: [
    MenuBar,
    MenuCol,
    BalanceComponent,
  ],
  templateUrl: './summary.page.html',
  styleUrl: './summary.page.css',
})
export class SummaryPage {

}
