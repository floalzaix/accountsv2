import { Component } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { CardModule } from 'primeng/card';

@Component({
  selector: 'app-catgory-component',
  imports: [
    ButtonModule,
    CardModule,
  ],
  templateUrl: './catgory.component.html',
  styleUrl: './catgory.component.css',
})
export class CatgoryComponent {

}
