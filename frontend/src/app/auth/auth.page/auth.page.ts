import { Component } from '@angular/core';
import { AuthComponent } from '../auth.component/auth.component';

@Component({
  selector: 'app-auth-page',
  imports: [AuthComponent],
  templateUrl: './auth.page.html',
  styleUrl: './auth.page.css',
})
export class AuthPage {}
