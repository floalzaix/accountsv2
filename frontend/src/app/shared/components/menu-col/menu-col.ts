import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-menu-col',
  imports: [
    ButtonModule,
  ],
  templateUrl: './menu-col.html',
  styleUrl: './menu-col.css',
})
export class MenuCol {
  //
  //   Interfaces
  //
  
  protected readonly router = inject(Router);
}
