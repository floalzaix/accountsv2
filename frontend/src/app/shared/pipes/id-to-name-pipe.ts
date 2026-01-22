import { Pipe, PipeTransform } from '@angular/core';
import { Category } from '../../categories/categories.model';

@Pipe({
  name: 'idToName',
})
export class IdToNamePipe implements PipeTransform {
  transform(id: string, map: Record<string, { name: string }>): string | null {
    return map[id]?.name ?? null;
  }
}
