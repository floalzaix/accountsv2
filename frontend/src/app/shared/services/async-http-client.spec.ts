import { TestBed } from '@angular/core/testing';

import { AsyncHttpClient } from './async-http-client';

describe('AsyncHttpClient', () => {
  let service: AsyncHttpClient;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AsyncHttpClient);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
