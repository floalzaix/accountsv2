import { Component } from '@angular/core';
import { Options } from '../../components/options/options';
import { DetailsTab } from '../../../details/details-tab/details-tab';
import { MenuBar } from '../../components/menu-bar/menu-bar';
import { MenuCol } from '../../components/menu-col/menu-col';

@Component({
  selector: 'app-details.page',
  imports: [
    Options,
    DetailsTab,
    MenuBar,
    MenuCol,
  ],
  templateUrl: './details.page.html',
  styleUrl: './details.page.css',
})
export class DetailsPage {

}
