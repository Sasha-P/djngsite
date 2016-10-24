import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard.component';
import { HeroesComponent } from './heroapp/heroes.component';
import { HeroDetailComponent } from './heroapp/hero-detail.component';
import { HeroService } from './heroapp/hero.service';
import { PostsComponent } from './blogapp/posts.component';
import { PostDetailComponent } from './blogapp/post-detail.component';
import { PostService } from './blogapp/post.service';


@NgModule({
    imports: [ 
        BrowserModule, 
        FormsModule,
        HttpModule,
        AppRoutingModule
    ],
    declarations: [ 
        AppComponent,
        DashboardComponent,
        HeroDetailComponent,
        HeroesComponent,
        PostDetailComponent,
        PostsComponent
    ],
    providers: [
        HeroService,
        PostService
    ],
    bootstrap: [ AppComponent ]
})
export class AppModule { }