use bbs;

DROP TABLE IF EXISTS `users` ;

CREATE TABLE IF NOT EXISTS `users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `name` NVARCHAR(20) NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;



DROP TABLE IF EXISTS posts ;

CREATE TABLE IF NOT EXISTS posts (
  `post_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `title` NVARCHAR(255) NULL,
  `content` NVARCHAR(1000) NULL,
  `date` DATETIME NOT NULL,
  PRIMARY KEY (`post_id`),
  CONSTRAINT `fk_post_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
