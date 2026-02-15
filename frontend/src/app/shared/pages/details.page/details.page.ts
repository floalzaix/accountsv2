import { Component, effect, inject, OnInit, signal } from '@angular/core';
import { DetailsTab } from '../../../details/details-tab/details-tab';
import { SelectButtonModule } from 'primeng/selectbutton';
import { FormsModule } from '@angular/forms';
import { OptionsService } from '../../services/options';

@Component({
  selector: 'app-details.page',
  imports: [
    DetailsTab,
    SelectButtonModule,
    FormsModule,
  ],
  templateUrl: './details.page.html',
  styleUrl: './details.page.css',
})
export class DetailsPage implements OnInit {
  //
  //   Data
  //
  
  protected selectedTab = signal<"revenues" | "expenses" | "differences">("revenues");
  protected readonly optionsService = inject(OptionsService);

  //
  //   Effects
  //
  
  protected readonly selectedTabEffect = effect(() => {
    if (!this.selectedTab()) {
      setTimeout(() => {
        this.selectedTab.set("revenues");
      }, 1);
    }
  });
  
  //
  //   Init 
  //
  
  ngOnInit(): void {
    this.optionsService.multiple.set(true);
  }
}
