import game

def init_logging(filename: str = None):
        level = logbook.TRACE

        if filename:
            logbook.TimedRotatingFileHandler(filename, level=level).push_application()
        else:
            logbook.StreamHandler(sys.stdout, level=level).push_application()
            
        msg = 'Logging initialized, level: {}, mode: {}'.format(
            level,
            "stdout mode" if not filename else 'file mode: ' + filename
        )
        logger = logbook.Logger('Startup')
        logger.notice(msg)

if __name__ == '__main__':
    init_logging("first_log.log")
    game = game.Game()
    game.main()

    # print("Which game wanna play? Normal or 15")
    # input_user = input("- ")
    # if input_user == 'Normal':
    #     game = game.Game()
    #     game.main()
    # else:
    #     game = game_15.Game()
    #     game.main()
