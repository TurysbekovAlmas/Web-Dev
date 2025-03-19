import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnChanges {
  @Input() photos: { id: number, title: string, url: string }[] = [];

  ngOnChanges(changes: SimpleChanges) {
    console.log('Изменение входных данных:', changes['photos']);
  }

  onImageError(photo: { url: string }) {
    photo.url = 'https://i.pinimg.com/originals/fd/2a/2f/fd2a2f0e44ad8561c3c90a16a24b59b2.jpg'; // Заменяем нерабочее изображение на заглушку
  }
}
