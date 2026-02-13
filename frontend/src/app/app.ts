import { Component, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MenuBar } from "./shared/components/menu-bar/menu-bar";
import { MenuCol } from "./shared/components/menu-col/menu-col";
import { AuthService } from "./auth/auth.service";
import { OptionsService } from "./shared/services/options";

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    MenuBar,
    MenuCol,
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  //
  //   Interfaces
  //
  
  protected readonly authService = inject(AuthService);
  protected readonly optionsService = inject(OptionsService);

  //
  //   Data
  //
  
  
  protected readonly title = signal('accounts-v2');
}
