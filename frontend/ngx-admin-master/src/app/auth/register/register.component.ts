import {ChangeDetectorRef, Component, Inject} from '@angular/core';
import {NB_AUTH_OPTIONS, NbAuthService, NbRegisterComponent} from '@nebular/auth';
import {AuthService} from '../services/auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'ngx-register',
  templateUrl: './register.component.html',
})
export class NgxRegisterComponent extends NbRegisterComponent {

  constructor(service: NbAuthService, @Inject(NB_AUTH_OPTIONS) options: {},
              cd: ChangeDetectorRef, router: Router, private auth: AuthService) {
    super(service, options, cd, router);
    localStorage.setItem('token', null);
    localStorage.setItem('user', null);
  }

  register() {
    // console.log(this.user);
    this.auth.register(this.user);
  }
}
