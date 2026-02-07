import { inject, Injectable } from '@angular/core';
import { AsyncHttpClient } from '../shared/services/async-http-client';
import { BehaviorSubject, map, Observable, switchMap } from 'rxjs';
import { DetailsTab, DetailsTabRow, DetailsTabSchema } from './details-tab-model';
import { toSignal } from '@angular/core/rxjs-interop';
import { OptionsService } from '../shared/services/options';
import { TreeNode } from 'primeng/api';

@Injectable({
  providedIn: 'root',
})
export class DetailsService {
  //
  //   Interfaces
  //
  
  private readonly client = inject(AsyncHttpClient);
  private readonly opionsService = inject(OptionsService);

  //
  //   Methods
  //

  /**
   * Converts the DetailsTab to the PrimeNG format for
   * TreeTable => Just renames the values into data and
   * the child_rows into children.
   * 
   * @param row The row to convert to a node treeNode
   * @returns The converted row
   */
  private toTreeNode(row: DetailsTabRow): TreeNode {
    const treeNode = {
      data: row.values,
      children: row.child_rows?.map((childRow) => {
        return this.toTreeNode(childRow)
      })
    }

    return treeNode
  }
  
  public getDetailsTabAndNodes(
    tab_type: "revenues" | "expenses" | "differences",
  ): Observable<[DetailsTab, TreeNode[]]> {
    return this.client.get<DetailsTab>(
      "/details",
      {
        "year": this.opionsService.year(),
        "tab_type": tab_type,
        "trans_types": this.opionsService.multipleTypes() ?? [],
      }
    ).pipe(
      map((response) => {
        const detailsTab = DetailsTabSchema.parse(response);

        const treeNode = detailsTab.rows.map((row) => {
          return this.toTreeNode(row);
        })

        return [detailsTab, treeNode]
      })
    );
  }

  //
  //   Refreshable data
  //
  
  private readonly refreshTrigger = new BehaviorSubject<void>(undefined);

  public refresh(): void {
    this.refreshTrigger.next();
  }

  public revenuesTab = toSignal(
    this.refreshTrigger.pipe(
      switchMap(() => this.getDetailsTabAndNodes("revenues"))
    )
  );

  public expensesTab = toSignal(
    this.refreshTrigger.pipe(
      switchMap(() => this.getDetailsTabAndNodes("expenses"))
    )
  );

  public differencesTab = toSignal(
    this.refreshTrigger.pipe(
      switchMap(() => this.getDetailsTabAndNodes("differences"))
    )
  );
}
