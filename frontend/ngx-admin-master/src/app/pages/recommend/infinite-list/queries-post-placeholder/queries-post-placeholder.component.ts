import { Component, HostBinding } from '@angular/core';

@Component({
  selector: 'ngx-queries-post-placeholder',
  templateUrl: 'queries-post-placeholder.component.html',
  styleUrls: ['queries-post-placeholder.component.scss'],
})
export class QueriesPostPlaceholderComponent {

  @HostBinding('attr.aria-label')
  label = 'Loading';
}
