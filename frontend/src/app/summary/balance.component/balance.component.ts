import { Component, computed, inject } from '@angular/core';
import { SummaryService } from '../summary.service';
import { KnobModule } from 'primeng/knob';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-balance',
  imports: [
    KnobModule,
    FormsModule,
  ],
  templateUrl: './balance.component.html',
  styleUrl: './balance.component.css',
})
export class BalanceComponent {
  //
  //   Interfaces
  //
  
  protected readonly summaryService = inject(SummaryService);

  //
  //   Data
  //
  
  protected readonly abs = computed(() => {
    return Math.abs(this.summaryService.balance() || 0) + 500;
  })
}
