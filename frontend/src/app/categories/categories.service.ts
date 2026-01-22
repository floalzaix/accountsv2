import { computed, inject, Injectable } from '@angular/core';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { BehaviorSubject, catchError, Observable, switchMap } from 'rxjs';
import { Category } from './categories.model';
import { toSignal } from '@angular/core/rxjs-interop';

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

  //
  //   Refreshable data
  //

  private readonly refreshTrigger = new BehaviorSubject<void>(undefined);
  
  /**
   * The purpose of this section is to allow every component dependent
   * on the list of categories to be refreshed thanks to the refreshed
   * method at first. Fo instance you have two components depending on the
   * list of categories, you can call the refreshed method and both will
   * be refreshed.
   */
  public refresh(): void {
    this.refreshTrigger.next();
  }

  public categories = toSignal(
    this.refreshTrigger.pipe(
      switchMap(() => this.getAllCategories())
    )
  );

  public categoriesMap = computed<Record<string, Category>>(() => {
    const categories = this.categories();

    if (!categories) {
      return {};
    }
    
    return categories.reduce((acc, category) => {
      acc[category.id] = category;
      return acc;
    }, {} as Record<string, Category>);
  });
}
