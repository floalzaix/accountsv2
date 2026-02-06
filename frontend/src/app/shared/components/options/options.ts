import { Component, inject, input } from '@angular/core';
import { OptionsService } from '../../services/options';
import { ListboxModule } from 'primeng/listbox';
import { FormsModule } from '@angular/forms';
import { DetailsService } from '../../../details/details-service';
import { SummaryService } from '../../../summary/summary.service';

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
  protected readonly detailsService = inject(DetailsService);
  protected readonly summaryService = inject(SummaryService);

  // INPUTS

  public readonly multiple = input<boolean>(false);
  
  //
  //   Data
  //
  
  public readonly YEARS = Array.from(
    { length: new Date().getFullYear() + 1 - 2026 },
    (_, index) => new Date().getFullYear() + index
  );
}
