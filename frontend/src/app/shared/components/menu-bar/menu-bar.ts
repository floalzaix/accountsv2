import { Component, inject } from '@angular/core';
import { AuthService } from '../../../auth/auth.service';
import { ButtonModule } from 'primeng/button';

@Component({
  selector: 'app-menu-bar',
  imports: [
    ButtonModule,
  ],
  templateUrl: './menu-bar.html',
  styleUrl: './menu-bar.css',
})
export class MenuBar {
  //
  //   Interfaces
  //
  
  protected readonly authService = inject(AuthService);
}
