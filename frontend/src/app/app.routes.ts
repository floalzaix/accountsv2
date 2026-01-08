import { Routes } from '@angular/router';
import { AuthPage } from './auth/auth.page/auth.page';
import { HomePage } from './shared/pages/home.page/home.page';
import { authGuardGuard } from './shared/guards/auth-guard-guard';

export const routes: Routes = [
    {
        path: "auth",
        component: AuthPage,
    },
    {
        path: "home",
        component: HomePage,
        canActivate: [authGuardGuard],
    },
    {
        path: "**",
        redirectTo: "auth",
    }
];
