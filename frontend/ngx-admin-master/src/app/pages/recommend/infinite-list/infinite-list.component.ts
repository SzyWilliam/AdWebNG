import { Component } from '@angular/core';
import { QueryFetcher } from '../recommend.service';

@Component({
  selector: 'ngx-queries-post-list',
  templateUrl: 'infinite-list.component.html',
  styleUrls: ['infinite-list.component.scss'],
})
export class InfiniteListComponent {
  firstCard = {
    news: [],
    placeholders: [],
    loading: false,
    pageToLoadNext: 1,
  };
  secondCard = {
    news: [],
    placeholders: [],
    loading: false,
    pageToLoadNext: 1,
  };
  pageSize = 10;

  constructor(private queryFetcher: QueryFetcher) {}

  loadNext(cardData) {
    if (cardData.loading) { return; }

    cardData.loading = true;
    cardData.placeholders = new Array(this.pageSize);
    this.queryFetcher.load(cardData.pageToLoadNext, this.pageSize)
      .subscribe(nextQueries => {
        cardData.placeholders = [];
        cardData.news.push(...nextQueries);
        cardData.loading = false;
        cardData.pageToLoadNext++;
      });
  }
}
