import { ErrorHandler, inject, Injectable } from "@angular/core";
import { Router } from "@angular/router";

@Injectable()
export class GlobalErrorHandler extends ErrorHandler {
  //
  //   Interfaces
  //
  private readonly router = inject(Router);
  
  //
  //   Overrides
  //
  
  override handleError(error: any): void {
    console.error("Unhandled error:", error);
  }
}