import { Routes } from '@angular/router';
import { AuthPage } from './auth/auth.page/auth.page';
import { HomePage } from './shared/pages/home.page/home.page';
import { authGuard } from './shared/guards/auth-guard';
import { DetailsPage } from './shared/pages/details.page/details.page';
import { SummaryPage } from './shared/pages/summary.page/summary.page';

export const routes: Routes = [
    {
        path: "auth",
        component: AuthPage,
    },
    {
        path: "home",
        component: HomePage,
        canActivate: [authGuard],
    },
    {
        path: "details",
        component: DetailsPage,
        canActivate: [authGuard],
    },
    {
        path: "summary",
        component: SummaryPage,
        canActivate: [authGuard],
    },
    {
        path: "**",
        redirectTo: "auth",
    }
];
