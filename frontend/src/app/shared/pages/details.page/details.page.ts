import { Component } from '@angular/core';
import { Options } from '../../components/options/options';
import { DetailsTab } from '../../../details/details-tab/details-tab';

@Component({
  selector: 'app-details.page',
  imports: [
    Options,
    DetailsTab,
  ],
  templateUrl: './details.page.html',
  styleUrl: './details.page.css',
})
export class DetailsPage {

}
