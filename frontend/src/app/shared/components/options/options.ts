import { Component, effect, inject, input } from '@angular/core';
import { ListboxModule } from 'primeng/listbox';
import { FormsModule } from '@angular/forms';
import { OptionsService } from '../../services/options';
import { SummaryService } from '../../../summary/summary.service';
import { DetailsService } from '../../../details/details-service';
import { TransactionsService } from '../../../transactions/trans.service';

@Component({
  selector: 'app-options',
  imports: [
    ListboxModule,
    FormsModule
  ],
  templateUrl: './options.html',
  styleUrl: './options.css',
})
export class Options {
  //
  //   Interfaces
  //

  protected readonly optionsService = inject(OptionsService);
  protected readonly summaryService = inject(SummaryService);
  protected readonly detailsService = inject(DetailsService);
  protected readonly transactionsService = inject(TransactionsService);
  
  // INPUTS

  public readonly multiple = input<boolean>(false);
  
  //
  //   Data
  //
  
  public readonly YEARS = Array.from(
    { length: new Date().getFullYear() + 1 - 2026 },
    (_, index) => new Date().getFullYear() + index
  );

  //
  //   Effects
  //
  
  private readonly refreshEffect = effect(() => {
    if (this.optionsService.multipleTypes().length > 0) {
      this.summaryService.refresh();
      this.detailsService.refresh();
    }

    if (this.optionsService.types() && this.optionsService.year()) {
      this.detailsService.refresh();
      this.summaryService.refresh();
      this.transactionsService.refresh();
    }
    
  });
}
