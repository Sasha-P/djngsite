import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

import { Hero } from './heroapp/hero';
import { HeroService } from './heroapp/hero.service';
import { Post } from './blogapp/post';
import { PostService } from './blogapp/post.service';

@Component({
    moduleId: module.id,
    selector: 'my-dashboard',
    templateUrl: 'dashboard.component.html',
    styleUrls: [ 'dashboard.component.css' ]
})
export class DashboardComponent implements OnInit {

    heroes: Hero[] = [];
    posts: Post[] = [];

    constructor(
        private router: Router,
        private heroService: HeroService,
        private postService: PostService
    ) { }

    ngOnInit(): void {
        this.heroService.getHeroes().then(heroes => this.heroes = heroes.slice(1, 5));
        this.postService.getPosts().then(posts => this.posts = posts.slice(1, 5));
    }

    gotoHeroDetail(hero: Hero): void {
        let link = ['/detail', hero.id];
        this.router.navigate(link);
    }

    gotoPostDetail(post: Post): void {
        let link = ['/post', post.id];
        this.router.navigate(link);
    }
}