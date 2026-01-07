import { TestBed } from '@angular/core/testing';

import { ValidationError } from './validation-error';

describe('ValidationError', () => {
  let service: ValidationError;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ValidationError);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
