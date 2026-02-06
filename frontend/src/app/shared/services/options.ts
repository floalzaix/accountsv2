import { effect, Injectable, signal } from '@angular/core';
import { Type } from '../enums/type';

@Injectable({
  providedIn: 'root',
})
export class OptionsService {
  //
  //   Constants
  //
  
  public readonly typeValues = [
    { label: "Courant", value: Type.CHECKING },
    { label: "Epargne", value: Type.SAVINGS },
    { label: "Espèces", value: Type.CASH },
  ];
  
  //
  //   Global attributes
  //

  public readonly multipleTypes = signal<Type[]>([Type.CHECKING]);
  
  public readonly types = signal<Type>(Type.CHECKING);
  public readonly year = signal<number>(new Date().getFullYear());

  //
  //   Effects
  //

  private previousMultipleTypes = this.multipleTypes();
  private readonly multipleTypesValidator = effect(() => {
    if (this.multipleTypes().length > 0) {
      this.previousMultipleTypes = this.multipleTypes();
    } else {
      setTimeout(() => {
        this.multipleTypes.set(this.previousMultipleTypes);
      }, 10);
    }
  });

  private previousType = this.types();
  private readonly typeValidator = effect(() => {
    if (this.types()) {
      this.previousType = this.types();
    } else {
      setTimeout(() => {
        this.types.set(this.previousType);
      }, 10);
    }
  });
  
  private previousYear = this.year();
  private readonly yearValidator = effect(() => {
    if (this.year()) {
      this.previousYear = this.year();
    } else {
      setTimeout(() => {
        this.year.set(this.previousYear);
      }, 10);
    }
  });
}
