import { Component, inject, input } from '@angular/core';
import { AuthService } from '../../../auth/auth.service';
import { ButtonModule } from 'primeng/button';
import { Options } from '../options/options';

@Component({
  selector: 'app-menu-bar',
  imports: [
    ButtonModule,
    Options,
  ],
  templateUrl: './menu-bar.html',
  styleUrl: './menu-bar.css',
})
export class MenuBar {
  //
  //   Interfaces
  //
  
  protected readonly authService = inject(AuthService);

  // INPUTS

  public readonly multipleOptions = input<boolean>(false);
}
