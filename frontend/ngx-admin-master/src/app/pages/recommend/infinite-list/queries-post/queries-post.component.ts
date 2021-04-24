import { Component, Input } from '@angular/core';

import { QueryPost } from '../../recommend.service';

@Component({
  selector: 'ngx-queries-post',
  templateUrl: 'queries-post.component.html',
})
export class QueriesPostComponent {

  @Input() post: QueryPost;
}
