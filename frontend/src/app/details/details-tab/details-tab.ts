import { Component, computed, inject, input } from '@angular/core';
import { DetailsService } from '../details-service';
import { TreeTableModule } from 'primeng/treetable';

@Component({
  selector: 'app-details-tab',
  imports: [
    TreeTableModule,
  ],
  templateUrl: './details-tab.html',
  styleUrl: './details-tab.css',
})
export class DetailsTab {
  //
  //   Interfaces
  //
  
  protected readonly detailsService = inject(DetailsService);

  // INPUTS

  public tab_type = input.required<"revenues" | "expenses" | "differences">();

  //
  //   Data
  //
  
  protected readonly details = computed(() => {
    switch (this.tab_type()) {
      case "revenues":
        return this.detailsService.revenuesTab();
      case "expenses":
        return this.detailsService.expensesTab();
      case "differences":
        return this.detailsService.differencesTab();
      default:
        return undefined;
    }
  })
}
