import { Component, inject, input } from '@angular/core';
import { Router } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { Options } from '../options/options';

@Component({
  selector: 'app-menu-col',
  imports: [
    ButtonModule,
    Options,
  ],
  templateUrl: './menu-col.html',
  styleUrl: './menu-col.css',
})
export class MenuCol {
  //
  //   Interfaces
  //
  
  protected readonly router = inject(Router);

  // INPUTS

  public readonly multipleOptions = input<boolean>(false);
}
