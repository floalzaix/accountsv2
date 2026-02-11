import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MenuBar } from "./shared/components/menu-bar/menu-bar";
import { MenuCol } from "./shared/components/menu-col/menu-col";

@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet,
    MenuBar,
    MenuCol
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('accounts-v2');
}
