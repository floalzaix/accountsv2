import { Component, inject, OnInit } from '@angular/core';
import { BalanceComponent } from '../../../summary/balance.component/balance.component';
import { OptionsService } from '../../services/options';

@Component({
  selector: 'app-summary.page',
  imports: [
    BalanceComponent,
  ],
  templateUrl: './summary.page.html',
  styleUrl: './summary.page.css',
})
export class SummaryPage implements OnInit {
  //
  //   Interfaces
  //
  
  protected readonly optionsService = inject(OptionsService);

  //
  //   Init 
  //
  
  ngOnInit(): void {
    this.optionsService.multiple.set(true);
  }
}
