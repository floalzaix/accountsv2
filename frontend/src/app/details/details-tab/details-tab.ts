import { Component, inject } from '@angular/core';
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
}
