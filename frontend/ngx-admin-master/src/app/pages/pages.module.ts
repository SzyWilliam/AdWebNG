import { NgModule } from '@angular/core';
import {NbCardModule, NbCheckboxModule, NbListModule, NbMenuModule} from '@nebular/theme';

import { ThemeModule } from '../@theme/theme.module';
import { PagesComponent } from './pages.component';

import { DashboardModule } from './dashboard/dashboard.module';
import { ECommerceModule } from './e-commerce/e-commerce.module';
import { PagesRoutingModule } from './pages-routing.module';
import { MiscellaneousModule } from './miscellaneous/miscellaneous.module';

import { SearchComponent } from './search/search.component';

import { RecommendComponent } from './recommend/recommend.component';
import { QueriesPostComponent } from './recommend/infinite-list/queries-post/queries-post.component';
import { QueriesPostPlaceholderComponent } from './recommend/infinite-list/queries-post-placeholder/queries-post-placeholder.component';
import { QueryFetcher } from './recommend/recommend.service';
import { InfiniteListComponent } from './recommend/infinite-list/infinite-list.component';
import { AuthService } from '../auth/services/auth.service';


@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    NbMenuModule,
    DashboardModule,
    ECommerceModule,
    MiscellaneousModule,
    NbListModule,
    NbCardModule,
    NbCheckboxModule,
  ],
  declarations: [
    PagesComponent,
    RecommendComponent,
    SearchComponent,
    QueriesPostComponent,
    QueriesPostPlaceholderComponent,
    InfiniteListComponent,
  ],
  providers: [
    QueryFetcher,
    AuthService,
  ],
})
export class PagesModule {
}
