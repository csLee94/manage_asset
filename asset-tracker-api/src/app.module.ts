import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { LibDbModule } from './libs/lib-db.module';

@Module({
  imports: [LibDbModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
