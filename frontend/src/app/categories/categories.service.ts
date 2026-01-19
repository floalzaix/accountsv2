import { inject, Injectable } from '@angular/core';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { catchError, Observable } from 'rxjs';
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

  public addCategory({  
    name,
    level,
    parent_id,
  }: {
    name: string,
    level: number,
    parent_id: string | null,
  }): Observable<unknown> {
    //
    //   Preparing the observable
    //
    const observable = this.http.post({
      endpoint: "/categories",
      json: {
        name,
        level,
        parent_id,
      },
    });

    return observable
  }

  public editCategory(id: string, name: string): Observable<unknown> {
    //
    //   Preparing the observable
    //
    const observable = this.http.put({
      endpoint: `/categories/${id}`,
      json: { name },
    });

    return observable;
  }

  public deleteCategory(id: string): Observable<unknown> {
    //
    //   Preparing the observable
    //
    const observable = this.http.delete(`/categories/${id}`);

    return observable;
  }
}
