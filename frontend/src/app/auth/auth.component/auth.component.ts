import { Component, inject } from '@angular/core';
import { AuthService } from '../auth.service';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { FloatLabel } from 'primeng/floatlabel';
import { ButtonModule } from 'primeng/button';
import { SelectButtonModule } from 'primeng/selectbutton';
import { ToastModule } from 'primeng/toast';
import { MessageService } from 'primeng/api';
import { User } from '../user.model';
import { ErrorWrapper } from '../../shared/errors/error-wrapper';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth-component',
  imports: [
    ReactiveFormsModule,
    InputTextModule,
    FloatLabel,
    ButtonModule,
    SelectButtonModule,
    ToastModule,
    FormsModule,
  ],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.css',
  providers: [MessageService],
})
export class AuthComponent {
  //
  //   Interfaces
  //
  
  private readonly authService: AuthService = inject(AuthService);
  private readonly toastService: MessageService = inject(MessageService);
  private readonly router: Router = inject(Router);
  
  //
  //   State
  //
  
  protected stateSelect: string = "login";

  //
  //   Forms
  //
  
  protected readonly registerForm: FormGroup = new FormGroup({
    email: new FormControl<string>(
      '', [Validators.required, Validators.email]
    ),
    password: new FormControl<string>(
      '', [Validators.required, Validators.minLength(8)]
    ),
    confirmPassword: new FormControl<string>(
      '', [Validators.required, Validators.minLength(8)]
    ),
    pseudo: new FormControl<string>(
      '', [Validators.required, Validators.minLength(1)]
    ),
  });

  protected readonly loginForm: FormGroup = new FormGroup({
    email: new FormControl<string>(
      '', [Validators.required, Validators.email]
    ),
    password: new FormControl<string>(
      '', [Validators.required, Validators.minLength(8)]
    ),
  });

  //
  //   Methods
  //
  
  protected register(): void {
    this.authService.register(this.registerForm.value).subscribe({
      next: (user: User) => {
        this.toastService.add({
          severity: "success",
          summary: "Inscription réussie",
          detail: "Bienvenue " + user.pseudo + " !",
        });
      },
      error: (error: ErrorWrapper) => {
        this.toastService.add({
          severity: "error",
          summary: error.userSafeTitle,
          detail: error.userSafeDescription,
          life: 2000,
        });
      },
    });
  }

  protected login(): void {
    this.authService.login(this.loginForm.value).subscribe({
      next: (user) => {
        this.toastService.add({
          severity: "success",
          summary: "Connexion réussie",
          detail: "Bienvenue " + user.pseudo + " !",
          life: 2000,
        });
        this.router.navigate(["/home"]);
      },
      error: (error: ErrorWrapper) => {
        this.toastService.add({
          severity: "error",
          summary: error.userSafeTitle,
          detail: error.userSafeDescription,
          life: 3000
,        });
      },
    });
  }
}
