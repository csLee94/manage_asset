import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { existsSync, mkdirSync, writeFileSync } from 'fs';
import { join } from 'path';

@Module({
  imports: [
    TypeOrmModule.forRootAsync({
      useFactory: () => {
        const projectRoot = join(__dirname, '..', '..');
        const dbDir = join(projectRoot, 'src', 'libs', 'db');
        const dbFile = join(dbDir, 'mydb.db');

        // db 디렉토리가 없으면 생성
        if (!existsSync(dbDir)) {
          mkdirSync(dbDir, { recursive: true });
        }

        // mydb.db 파일이 없으면 빈 파일 생성
        if (!existsSync(dbFile)) {
          writeFileSync(dbFile, '');
        }

        return {
          type: 'sqlite',
          database: dbFile,
          entities: [join(__dirname, '..', '**', '*.entity.ts')],
          synchronize: true, // 주의: 프로덕션 환경에서는 false로 설정해야 합니다.
        };
      },
    }),
  ],
})
export class LibDbModule {}
