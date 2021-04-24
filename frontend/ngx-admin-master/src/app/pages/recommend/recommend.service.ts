import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {delay, map} from 'rxjs/operators';

export class QueryPost {
  title: string;
  link: string;
  creator: string;
  text: string;
}

@Injectable()
export class QueryFetcher {

  constructor(private http: HttpClient) {}

  load(page: number, pageSize: number): Observable<QueryPost[]> {
    const startIndex = ((page - 1) % 7) * pageSize;

    return this.http
      .get<QueryPost[]>('assets/data/news.json')
      .pipe(
        map(news => news.splice(startIndex, pageSize)),
        delay(1500),
      );
  }
}
