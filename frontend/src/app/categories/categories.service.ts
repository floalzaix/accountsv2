import { inject, Injectable } from '@angular/core';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { Observable } from 'rxjs';
import { Category } from './categories.model';

@Injectable({
  providedIn: 'root',
})
export class CategoriesService {
  //
  //   Interfaces
  //
  
  private readonly http = inject(AsyncHttpClient);

  //
  //   Methods
  //
  
  public getAllCategories(): Observable<Category[]> {
    //
    //   Preparing the observable
    //
    const observable = this.http.get<Category[]>("/categories");

    return observable
  }
}
